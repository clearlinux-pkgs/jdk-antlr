Name     : jdk-antlr
Version  : 2.7.7
Release  : 3
URL      : http://www.antlr2.org/download/antlr-2.7.7.tar.gz
Source0  : http://www.antlr2.org/download/antlr-2.7.7.tar.gz
Source1  : http://repo2.maven.org/maven2/antlr/antlr/2.7.7/antlr-2.7.7.pom
Source2  : antlr-build.xml
Source3  : antlr-script
Summary  : No detailed summary available
Group    : Development/Tools
License  : ANTLR-PD
Patch0   : antlr-2.7.7-newgcc.patch
Patch1   : antlr-examples-license.patch
BuildRequires : apache-ant
BuildRequires : apache-maven
BuildRequires : doxygen
BuildRequires : graphviz
BuildRequires : javapackages-tools
BuildRequires : javapackages-tools
BuildRequires : jdk-aether
BuildRequires : jdk-aopalliance
BuildRequires : jdk-atinject
BuildRequires : jdk-cdi-api
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-guava
BuildRequires : jdk-guice
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-sisu
BuildRequires : jdk-slf4j
BuildRequires : jdk-wagon
BuildRequires : libpng
BuildRequires : lxml
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : openjdk-dev
BuildRequires : python-dev
BuildRequires : python3
BuildRequires : python3
BuildRequires : six
BuildRequires : six
BuildRequires : xmvn
BuildRequires : xmvn

%description
No detailed description available

%prep
%setup -q -n antlr-2.7.7
find . -name "*.jar" -exec rm -f {} \;
cp %{SOURCE2} build.xml

%patch0
%patch1 -p1

python3 /usr/share/java-utils/mvn_file.py antlr:antlr antlr

%build
ant -Dj2se.apidoc=/usr/share/javadoc/java
cp work/lib/antlr.jar .
export CLASSPATH=.

%configure
make

pushd lib/cpp
  doxygen doxygen.cfg
  find gen_doc -type f -exec chmod 0644 {} \;
popd

pushd lib/python
python2 setup.py build -b py2
popd

%install
python3 /usr/share/java-utils/mvn_artifact.py %{SOURCE1} work/lib/antlr.jar
python3 /usr/share/java-utils/mvn_alias.py antlr:antlr antlr:antlrall

xmvn-install  -R .xmvn-reactor -n antlr -d %{buildroot}

mkdir -p %{buildroot}{/usr/include/antlr,/usr/lib64,/usr/bin}
install -p -m 755 %{SOURCE3} %{buildroot}/usr/bin

install -p -m 644 lib/cpp/antlr/*.hpp %{buildroot}/usr/include/antlr
install -p -m 644 lib/cpp/src/libantlr.a %{buildroot}/usr/lib64
install -p -m 755 scripts/antlr-config %{buildroot}/usr/bin

pushd lib/python 
python2 -tt setup.py build -b py2 install --root=%{buildroot}
popd

%files
%defattr(-,root,root,-)
/usr/bin/antlr-config
/usr/bin/antlr-script
/usr/include/antlr
/usr/lib/python2.7/site-packages/antlr-2.7.5RC1-py2.7.egg-info
/usr/lib/python2.7/site-packages/antlr/__init__.py
/usr/lib/python2.7/site-packages/antlr/__init__.pyc
/usr/lib/python2.7/site-packages/antlr/antlr.py
/usr/lib/python2.7/site-packages/antlr/antlr.pyc
/usr/lib64/libantlr.a
/usr/share/java/antlr.jar
/usr/share/maven-metadata/antlr.xml
/usr/share/maven-poms/antlr.pom
