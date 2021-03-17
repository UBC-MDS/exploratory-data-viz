.PHONY: all

M1 = $(wildcard chapters/en/slides/module1/*.md)
M2 = $(wildcard chapters/en/slides/module2/*.md)
M3 = $(wildcard chapters/en/slides/module3/*.md)
M4 = $(wildcard chapters/en/slides/module4/*.md)
M5 = $(wildcard chapters/en/slides/module5/*.md)
M6 = $(wildcard chapters/en/slides/module6/*.md)
M7 = $(wildcard chapters/en/slides/module7/*.md)

## all : Regenerate all modules
all : $(M1) $(M2) $(M3) $(M4) $(M5) #$(M6) $(M7)

m1 : $(M1)
m2 : $(M2)
m3 : $(M3)
m4 : $(M4)
m5 : $(M5)
m6 : $(M6)
m7 : $(M7)

chapters/en/slides/module1/%.md : chapters/en/slides/module1/%.Rmd
	@echo
	@rm -rf static/module1/charts/$$(echo $@ | grep -oP "(?<=/module[0-9]_)[0-9]{2}(?=\.md)")/
	@echo "Removed previous chart files. Knitting and creating new charts..."
	Rscript format_slides.R --input=$<

chapters/en/slides/module2/%.md : chapters/en/slides/module2/%.Rmd
	@echo
	@rm -rf static/module2/charts/$$(echo $@ | grep -oP "(?<=/module[0-9]_)[0-9]{2}(?=\.md)")/
	@echo "Removed previous chart files. Knitting and creating new charts..."
	Rscript format_slides.R --input=$<

chapters/en/slides/module3/%.md : chapters/en/slides/module3/%.Rmd
	@echo
	@rm -rf static/module3/charts/$$(echo $@ | grep -oP "(?<=/module[0-9]_)[0-9]{2}(?=\.md)")/
	@echo "Removed previous chart files. Knitting and creating new charts..."
	Rscript format_slides.R --input=$<

chapters/en/slides/module4/%.md : chapters/en/slides/module4/%.Rmd
	@echo
	@rm -rf static/module4/charts/$$(echo $@ | grep -oP "(?<=/module[0-9]_)[0-9]{2}(?=\.md)")/
	@echo "Removed previous chart files. Knitting and creating new charts..."
	Rscript format_slides.R --input=$<

chapters/en/slides/module5/%.md : chapters/en/slides/module5/%.Rmd
	@echo
	@rm -rf static/module5/charts/$$(echo $@ | grep -oP "(?<=/module[0-9]_)[0-9]{2}(?=\.md)")/
	@echo "Removed previous chart files. Knitting and creating new charts..."
	Rscript format_slides.R --input=$<

chapters/en/slides/module6/%.md : chapters/en/slides/module6/%.Rmd
	@echo
	@rm -rf static/module6/charts/$$(echo $@ | grep -oP "(?<=/module[0-9]_)[0-9]{2}(?=\.md)")/
	@echo "Removed previous chart files. Knitting and creating new charts..."
	Rscript format_slides.R --input=$<

chapters/en/slides/module7/%.md : chapters/en/slides/module7/%.Rmd
	@echo
	@rm -rf static/module7/charts/$$(echo $@ | grep -oP "(?<=/module[0-9]_)[0-9]{2}(?=\.md)")/
	@echo "Removed previous chart files. Knitting and creating new charts..."
	Rscript format_slides.R --input=$<
