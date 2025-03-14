#
%define		module		tldextract
Summary:	Accurately separate the TLD from the registered domain and subdomains of a URL
Name:		python3-%{module}
Version:	3.4.4
Release:	3
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/tldextract/
Source0:	https://files.pythonhosted.org/packages/source/t/tldextract/%{module}-%{version}.tar.gz
# Source0-md5:	06617f12c12acc534517228d191928ef
URL:		https://github.com/john-kurkowski/tldextract/stargazers
BuildRequires:	python3
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Accurately separate the TLD from the registered domain and
subdomains of a URL, using the Public Suffix List. By default,
this includes the public ICANN TLDs and their exceptions. You can
optionally support the Public Suffix List's private domains as
well.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md
%attr(755,root,root) %{_bindir}/tldextract
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
