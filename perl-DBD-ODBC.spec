#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	ODBC
Summary:	DBD::ODBC perl module
Summary(pl):	Modu� perla DBD::ODBC
Name:		perl-DBD-ODBC
Version:	1.04
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-DBI > 1.20
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	unixODBC-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD::ODBC - DBD module interfacing the ODBC databases.

%description -l pl
DBD::ODBC - modu� DBD komunikuj�cy si� z bazami danych z u�yciem
ODBC.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL -o /usr

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
%{perl_sitearch}/DBD/ODBC.pm
%dir %{perl_sitearch}/auto/DBD/ODBC
%{perl_sitearch}/auto/DBD/ODBC/ODBC.bs
%attr(755,root,root) %{perl_sitearch}/auto/DBD/ODBC/ODBC.so
%{_mandir}/man3/*
