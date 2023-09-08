# Makefile to run the Python script and clean up

all: run_script

run_script:
	python3 ./generate-certificates.py

clean:
	-rm -f *.aux
	-rm -f *.log
	-rm -f temp.tex
	-rm -f temp.aux
	-rm -f temp.log

.PHONY: all run_script clean