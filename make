PACKAGE_NAME = TLS
VERSION = 1.0.0

.PHONY: all clean package_fedora package_ubuntu package_arch

all: clean package_fedora package_ubuntu package_arch

clean:
    rm -rf dist

package_fedora:
    python setup.py sdist
    cp dist/$(PACKAGE_NAME)-$(VERSION).tar.gz ~/rpmbuild/SOURCES/
    rpmbuild -bb packaging/fedora/$(PACKAGE_NAME).spec

package_ubuntu:
    python setup.py sdist
    cd dist && tar -xzvf $(PACKAGE_NAME)-$(VERSION).tar.gz
    cd dist/$(PACKAGE_NAME)-$(VERSION) && python setup.py --command-packages=stdeb.command sdist_dsc
    cd dist/$(PACKAGE_NAME)-$(VERSION)/deb_dist/ && dpkg-buildpackage -rfakeroot -uc -us

package_arch:
    python setup.py sdist
    cd dist && tar -xzvf $(PACKAGE_NAME)-$(VERSION).tar.gz
    cd dist/$(PACKAGE_NAME)-$(VERSION) && makepkg -f
