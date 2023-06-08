LIB_ANTLR ?= /usr/local/share/antlr.jar
ANTLR_TOOL ?= antlr
ANTLR_SCRIPT := MicroC.g4

all: compiler

compiler:

ifeq (,$(wildcard using-python))
compiler: compiler_java
else
compiler: compiler_python
endif

compiler_java:
	@echo "using Java"
	rm -rf build classes
	mkdir build classes
	$(ANTLR_TOOL) -o build $(ANTLR_SCRIPT)
	javac -cp $(CLASSPATH):$(LIB_ANTLR) -d classes java/*.java build/*.java

compiler_python:
	@echo "using Python"
	$(ANTLR_TOOL) -o build -Dlanguage=Python3 $(ANTLR_SCRIPT)

clean:
	rm -rf classes build
