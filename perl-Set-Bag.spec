%include	/usr/lib/rpm/macros.perl
%define	pdir	Set
%define	pnam	Bag
Summary:	Set::Bag - bag (multiset) class
Summary(pl):	Set::Bag - klasa prostego worka (wielu zbior�w)
Name:		perl-Set-Bag
Version:	1.008
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements a simple bag (multiset) class.

%description -l pl
Ten modu� jest implementacj� klasy prostego worka (wielu zbior�w).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%{perl_sitelib}/Set/Bag.pm
%{_mandir}/man3/*
