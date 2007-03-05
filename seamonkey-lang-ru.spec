%define	_lang	ru
%define	_reg	RU
%define	_lare	%{_lang}-%{_reg}
Summary:	Russian resources for SeaMonkey
Summary(pl):	Rosyjskie pliki jêzykowe dla SeaMonkeya
Name:		seamonkey-lang-%{_lang}
Version:	1.1.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/contrib-localized/seamonkey-%{version}.%{_lare}.langpack.xpi
# Source0-md5:	75dd88deaff6dc9866c176b33e79101d
Source1:	http://www.mozilla-enigmail.org/downloads/lang/0.9x/enigmail-%{_lare}-0.9x.xpi
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
%{__unzip} -o -qq %{SOURCE1}
install %{SOURCE2} .
./gen-installed-chrome.sh locale chrome/{%{_reg},%{_lare},%{_lang}-unix,enigmail-%{_reg}}.jar \
	> lang-%{_lang}-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install chrome/{%{_reg},%{_lare},%{_lang}-unix,enigmail-%{_reg}}.jar $RPM_BUILD_ROOT%{_chromedir}
install lang-%{_lang}-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}
cp -r searchplugins dictionaries defaults $RPM_BUILD_ROOT%{_datadir}/seamonkey

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/seamonkey-chrome+xpcom-generate

%postun
%{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_reg}.jar
%{_chromedir}/%{_lare}.jar
%{_chromedir}/%{_lang}-unix.jar
%{_chromedir}/enigmail-%{_reg}.jar
%{_chromedir}/lang-%{_lang}-installed-chrome.txt
%{_datadir}/seamonkey/searchplugins/*
%{_datadir}/seamonkey/defaults/messenger/%{_reg}
%{_datadir}/seamonkey/defaults/profile/%{_reg}
%{_datadir}/seamonkey/dictionaries/*
