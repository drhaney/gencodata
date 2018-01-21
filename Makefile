## 12/14/2017

TARGET	= gencodata
VERSION	= 0.2
DISTRO	= -py2.py3-none-any
WHEELDIR= dist

WHEELFILE= $(WHEELDIR)/$(TARGET)-$(VERSION)$(DISTRO).whl

PIP	= pip2

none:
	@echo "Make targets are list, dist, build, install, uninstall, clean, html, mdfiles."
	@echo ""

#
#	DOCUMENTS
#

# pythonic restructured Text files

rst:	 $(TARGET)/doc/HARTREE.rst $(TARGET)/doc/INSTALL.rst $(TARGET)/doc/MANUAL.rst README.rst

# html files for everything else

html:    $(TARGET)/doc/HARTREE.html $(TARGET)/doc/INSTALL.html $(TARGET)/doc/MANUAL.html README.html

# markdown files for github, included for completeness but not implicitly built

mdfiles: $(TARGET)/doc/HARTREE.md $(TARGET)/doc/INSTALL.md $(TARGET)/doc/MANUAL.md README.md

%.html:	%.rst
	rst2html.py $< $@

%.md:	%.rst
	pandoc --from=rst --to=markdown_github $< -o $@

list:
	$(PIP) list --user

#
# Install package locally in $USER/.local
#
install:
	$(PIP) install --user $(WHEELFILE)

uninstall:
	$(PIP) uninstall -y $(TARGET)

clean:
	rm -rf ./dist/ ./build/
	rm -f *.html $(TARGET)/*.html $(TARGET)/doc/*.html
	rm -f *.md $(TARGET)/*.md

#
# build distribution archive and wheel files
#
build:
	$(MAKE) html
	cp *.html $(TARGET)
	python setup.py sdist bdist_wheel

dist:
	$(MAKE) build
##
