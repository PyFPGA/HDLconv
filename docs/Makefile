SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = build
HELPERS       = $(BUILDDIR)/vhdl2vhdl $(BUILDDIR)/vhdl2vlog $(BUILDDIR)/slog2vlog

PYTHONPATH := $(PWD)/..
export PYTHONPATH

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

$(HELPERS):
	@mkdir -p $(@D)
	@python3 ../hdlconv/$(@F).py -h > $@

%: Makefile $(HELPERS)
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
