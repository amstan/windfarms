NAME=windfarms
PACKAGEZIP=$(NAME).zip
PACKAGEFOLDER=packagefolder

all: package install run

package:
	@echo zip -r $(PACKAGEZIP) $(PACKAGEFOLDER)/*
	@cd $(PACKAGEFOLDER) && zip -r ../$(PACKAGEZIP) .>/dev/null

install:
	plasmapkg -i $(PACKAGEZIP)

run: 
	@echo "run to be implemented, open the desktop activity settings manually"

clean: uninstall
	-rm -f $(PACKAGEZIP)

uninstall:
	plasmapkg -r $(NAME) --type wallpaperplugin
	-rm -r ~/.kde/share/kde4/services/plasma-wallpaper-windfarms.desktop
	-rm -r ~/.kde/share/apps/plasma/wallpapers//windfarms

test:
	@echo "not implemented yet"