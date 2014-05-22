PROJECT = Modello_Nav

VERSION := 0.0.2
PACKAGE = $(PROJECT)-$(VERSION)

INSTALL_FILES = $(PROJECT).wgt
INSTALL_DIR = ${DESTDIR}/opt/usr/apps/.preinstallWidgets

wgtPkg:
	zip -r $(PROJECT).wgt config.xml css Navigation_icon.png images index.html js templates

install:
	@echo "Installing Navigation, stand by..."
	mkdir -p $(INSTALL_DIR)/
	mkdir -p ${DESTDIR}/opt/usr/apps/_common/icons
	cp $(PROJECT).wgt $(INSTALL_DIR)/
	cp Navigation_icon.png ${DESTDIR}/opt/usr/apps/_common/icons

dist:
	tar czf ../$(PACKAGE).tar.bz2 .
