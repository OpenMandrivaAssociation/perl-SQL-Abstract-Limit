%define upstream_name	 SQL-Abstract-Limit
%define upstream_version 0.141

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Portable LIMIT emulation
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/SQL/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(DBI)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(SQL::Abstract) >= 1.20
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::More)

BuildArch:	noarch

%description
Portability layer for LIMIT emulation.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor destdir=%{buildroot}
./Build

%check
./Build test

%install
./Build install

%files
%doc Changes README
%{perl_vendorlib}/SQL
%{_mandir}/man*/*

%changelog
* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.141.0-3mdv2010.1
+ Revision: 505283
- rebuild using %%perl_convert_version

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.141-2mdv2010.0
+ Revision: 440637
- rebuild

* Sun Dec 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.141-1mdv2009.1
+ Revision: 320557
- update to new version 0.141

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.12-3mdv2008.1
+ Revision: 136347
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-3mdv2008.0
+ Revision: 86870
- rebuild


* Sun Aug 06 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-06 17:13:31 (53490)
- Rebuild for proper release suffix

* Sun Aug 06 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-06 17:09:10 (53487)
- import perl-SQL-Abstract-Limit-0.12-1mdk

* Mon May 22 2006 Scott Karns <scottk@mandriva.org> 0.12-1mdk
- First mandriva package

