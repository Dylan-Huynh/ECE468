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
	$(ANTLR_TOOL) -o build java/$(ANTLR_SCRIPT)
	javac -cp $(CLASSPATH):$(LIB_ANTLR) -d classes java/compiler/*.java java/ast/*.java java/assembly/*.java java/assembly/instructions/*.java java/ast/visitor/*.java build/java/*.java

compiler_python:
	@echo "using Python"
	$(ANTLR_TOOL) -o build -Dlanguage=Python3 python/$(ANTLR_SCRIPT)

clean:
	rm -rf classes build
