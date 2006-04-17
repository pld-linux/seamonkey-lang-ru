Summary:	Russian resources for SeaMonkey
Summary(pl):	Rosyjskie pliki jêzykowe dla SeaMonkeya
Name:		seamonkey-lang-ru
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/contrib-localized/seamonkey-%{version}.ru-RU.langpack.xpi
# Source0-md5:	cc413d89e9f2363eb16804c6cbeb00de
Source1:	http://www.mozilla-enigmail.org/downloads/lang/0.9x/enigmail-ru-RU-0.9x.xpi
# Source1-md5:	2febfba49fcc6819eb99997a7c2082ff
Source2:	gen-installed-chrome.sh
URL:		http://www.mozilla.org/projects/seamonkey/
BuildRequires:	unzip
Requires(post,postun):	seamonkey >= %{version}
Requires(post,postun):	textutils
Requires:	seamonkey >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_chromedir	%{_datadir}/seamonkey/chrome

%description
Russian resources for SeaMonkey.

%description -l pl
Rosyjskie pliki jêzykowe dla SeaMonkeya.

%prep
%setup -q -c
unzip -o %{SOURCE1}
install %{SOURCE2} .
./gen-installed-chrome.sh locale chrome/{RU,ru-RU,ru-unix,enigmail-RU}.jar \
	> lang-ru-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install chrome/{RU,ru-RU,ru-unix,enigmail-RU}.jar $RPM_BUILD_ROOT%{_chromedir}
install lang-ru-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}
cp -r searchplugins myspell defaults $RPM_BUILD_ROOT%{_datadir}/seamonkey

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/seamonkey-chrome+xpcom-generate

%postun
%{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/RU.jar
%{_chromedir}/ru-RU.jar
%{_chromedir}/ru-unix.jar
%{_chromedir}/enigmail-RU.jar
%{_chromedir}/lang-ru-installed-chrome.txt
%{_datadir}/seamonkey/searchplugins/*
%{_datadir}/seamonkey/defaults/messenger/RU
%{_datadir}/seamonkey/defaults/profile/RU
%{_datadir}/seamonkey/myspell/*
