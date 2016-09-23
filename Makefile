PKG_NAME := jdk-antlr
URL := http://www.antlr2.org/download/antlr-2.7.7.tar.gz
ARCHIVES := http://repo2.maven.org/maven2/antlr/antlr/2.7.7/antlr-2.7.7.pom %{buildroot} \
	antlr-build.xml %{buildroot} \
	antlr-script %{buildroot}

include ../common/Makefile.common
