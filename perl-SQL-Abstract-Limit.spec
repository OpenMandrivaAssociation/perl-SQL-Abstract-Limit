%define upstream_name	 SQL-Abstract-Limit
%define upstream_version 0.141

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:	Portable LIMIT emulation
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/SQL/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl(DBI)
BuildRequires:  perl(Module::Build)
BuildRequires:	perl(SQL::Abstract) >= 1.20
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::More)

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Portability layer for LIMIT emulation.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{perl_vendorlib}/SQL
%{_mandir}/man*/*
