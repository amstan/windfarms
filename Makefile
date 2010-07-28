NAME=windfarms
PACKAGEZIP=$(NAME).zip
PACKAGEFOLDER=packagefolder
TYPE=wallpaper

all: package install run

package:
	@echo "zip -r $(PACKAGEZIP) $(PACKAGEFOLDER)/*"
	@cd $(PACKAGEFOLDER) && zip -r ../$(PACKAGEZIP) .>/dev/null

install: package
	if [ ! -f ~/.kde/share/kde4/services/plasma-$(TYPE)-$(NAME).desktop ]; then plasmapkg -i $(PACKAGEZIP); fi
	cp code/* ~/.kde/share/apps/plasma/$(TYPE)s/$(NAME)/contents/code/
	@sleep 1

run: 
	@echo "run to be implemented, open the desktop activity settings manually"

clean: uninstall
	-rm -f $(PACKAGEZIP)
uninstall:
	plasmapkg -r $(NAME)
	#-rm -r ~/.kde/share/kde4/services/plasma-wallpaper-windfarms.desktop
	#-rm -r ~/.kde/share/apps/plasma/wallpapers//windfarms

test: install
	plasmoidviewer -c folderview -w $(NAME) luna