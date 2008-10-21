%define	_lang	ru
%define	_reg	RU
%define	_lare	%{_lang}-%{_reg}
Summary:	Russian resources for SeaMonkey
Summary(pl.UTF-8):	Rosyjskie pliki językowe dla SeaMonkeya
Name:		seamonkey-lang-%{_lang}
Version:	1.1.12
Release:	1
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		I18n
Source0:	http://releases.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/contrib-localized/seamonkey-%{version}.%{_lare}.langpack.xpi
# Source0-md5:	74feb18634d436ba72af52175a797571
Source1:	http://www.mozilla-enigmail.org/download/release/0.95/enigmail-%{_lare}-0.95.xpi
# Source1-md5:	323d5e3192772ca48671d74518899bc7
Source2:	gen-installed-chrome.sh
URL:		http://www.seamonkey-project.org/
BuildRequires:	unzip
Requires(post,postun):	seamonkey >= %{version}
Requires(post,postun):	textutils
Requires:	seamonkey >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_chromedir	%{_datadir}/seamonkey/chrome

%description
Russian resources for SeaMonkey.

%description -l pl.UTF-8
Rosyjskie pliki językowe dla SeaMonkeya.

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
