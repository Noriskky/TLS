PACKAGE_NAME = tls
VERSION = 0.1.0

.PHONY: all clean package_fedora package_debian

all: clean package_fedora package_debian

clean:
	rm -rf dist

package_fedora:
	python3 setup.py sdist
	cp dist/$(PACKAGE_NAME)-$(VERSION).tar.gz ~/rpmbuild/SOURCES/
	rpmbuild -bb packaging/fedora/$(PACKAGE_NAME).spec

package_debian:
	python3 setup.py --command-packages=stdeb.command sdist_dsc
	cd deb_dist/ && dpkg-buildpackage -rfakeroot -uc -us
