%include	/usr/lib/rpm/macros.perl
%define	pdir	Set
%define	pnam	Bag
Summary:	Set::Bag - bag (multiset) class
Summary(pl):	Set::Bag - klasa prostego worka (wielu zbiorów)
Name:		perl-Set-Bag
Version:	1.008
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7d568cef6ebc8c6a633f55cb8a8c70f4
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements a simple bag (multiset) class.

%description -l pl
Ten modu³ jest implementacj± klasy prostego worka (wielu zbiorów).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%{perl_vendorlib}/Set/Bag.pm
%{_mandir}/man3/*
