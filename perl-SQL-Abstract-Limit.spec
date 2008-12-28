%define module	SQL-Abstract-Limit
%define name	perl-%{module}
%define	modprefix SQL

%define version 0.141

%define	rel	1
%define release %mkrel %{rel}

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Portable LIMIT emulation
Url:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/SQL/%{module}-%{version}.tar.bz2
BuildRequires:	perl(DBI)
BuildRequires:  perl(Module::Build)
BuildRequires:	perl(SQL::Abstract) >= 1.20
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::More)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Portability layer for LIMIT emulation.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Build.PL installdirs=vendor destdir=%{buildroot}
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/%{modprefix}
%{_mandir}/man*/*
