#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	ODBC
Summary:	DBD::ODBC perl module
Summary(pl):	Modu³ perla DBD::ODBC
Name:		perl-DBD-ODBC
Version:	1.05
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	15fc684b7d658d73193fbab761d6b6f2
BuildRequires:	perl-DBI > 1.20
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	unixODBC-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD::ODBC - DBD module interfacing the ODBC databases.

%description -l pl
DBD::ODBC - modu³ DBD komunikuj±cy siê z bazami danych z u¿yciem
ODBC.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL -o /usr \
	INSTALLDIRS=vendor

%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{!?_without_tests:%{__make} test}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/DBD/ODBC.pm
%dir %{perl_vendorarch}/auto/DBD/ODBC
%{perl_vendorarch}/auto/DBD/ODBC/ODBC.bs
%attr(755,root,root) %{perl_vendorarch}/auto/DBD/ODBC/ODBC.so
%{_mandir}/man3/*
