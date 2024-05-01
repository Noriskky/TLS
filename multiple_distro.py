import subprocess
import os
import argparse
import shutil
import uuid

def download_docker_image(distro):
    try:
        if distro == "alpine":
            image_name = "alpine:latest"
        elif distro == "ubuntu":
            image_name = "ubuntu:latest"
        elif distro == "fedora":
            image_name = "fedora:latest"
        elif distro == "arch":
            image_name = "archlinux:latest"
        else:
            print("Unsupported distribution.")
            return None

        print(f"\033[94mDownloading Docker image for {distro}...\033[0m")
        subprocess.run(["docker", "pull", image_name])
        return image_name
    except FileNotFoundError:
        print("Required commands are not available. Make sure 'docker' command is installed.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None

def start_temp_shell(distro, hostname, command=None, directory=None, persistent=False):
    try:
        if directory:
            working_directory = os.path.abspath(os.path.join(os.getcwd(), directory))
        else:
            working_directory = f"/tmp/{distro}_temp_{uuid.uuid4().hex}"
            
        if not os.path.exists(working_directory):
            os.makedirs(working_directory)

        image_name = download_docker_image(distro)
        if not image_name:
            return

        # Extract the root filesystem from the Docker image
        print(f"\033[94mExtracting root filesystem for {distro}...\033[0m")
        subprocess.run(["docker", "create", "--name", f"{distro}_temp_container", image_name])
        subprocess.run(["docker", "cp", f"{distro}_temp_container:.", f"{working_directory}"])
        subprocess.run(["docker", "rm", f"{distro}_temp_container"])

        # Change the hostname
        print("\033[94mChanging hostname...\033[0m")
        subprocess.run(["sudo", "sh", "-c", f"echo '{hostname}' > {working_directory}/etc/hostname"])

        # Execute the specified command if provided
        if command:
            print(f"\033[94mExecuting command: {command}...\033[0m")
            subprocess.run(["sudo", "chroot", working_directory, "/bin/sh", "-c", command])
        else:
            # Execute chroot command to change root directory to the extracted distribution environment
            subprocess.run(["sudo", "chroot", working_directory, "/bin/sh", "-l"])
    except FileNotFoundError:
        print("Required commands are not available. Make sure 'docker', 'tar', 'chroot', and 'sh' commands are installed.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if not persistent:
            # Clear the temporary directory after exiting the shell
            print(f"\033[94mTemp directory cleared.\033[0m")
            if os.path.exists(working_directory):
                shutil.rmtree(working_directory)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start a temporary shell for a Linux distribution")
    parser.add_argument("--distro", "-d", choices=["alpine", "ubuntu", "fedora", "arch"], required=True, help="Specify the distribution (alpine, ubuntu, fedora, arch)")
    parser.add_argument("--hostname", "-hn", default="linux", help="Specify the hostname for the Linux environment")
    parser.add_argument("--command", "-c", help="Command to execute in the Linux environment")
    parser.add_argument("--directory", "-dir", help="Directory for the temporary environment")
    parser.add_argument("--persistent", "-p", help="Make the temporary environment persistent", action="store_true")
    args = parser.parse_args()

    if args.persistent and not args.directory:
        print("Make sure to specify a directory for persistent mode.")
        quit()

    start_temp_shell(args.distro, args.hostname, args.command, args.directory, args.persistent)
