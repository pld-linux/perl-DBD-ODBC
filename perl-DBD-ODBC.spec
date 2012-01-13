#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DBD
%define		pnam	ODBC
Summary:	DBD::ODBC - ODBC Driver for DBI
Summary(pl.UTF-8):	DBD::ODBC - sterownik DBI do ODBC
Name:		perl-DBD-ODBC
Version:	1.23
Release:	3
# GPL or Artistic as specified in perl README file
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DBD/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5ce4130a1c96995f730064f4d4b2836b
URL:		http://search.cpan.org/dist/DBD-ODBC/
BuildRequires:	perl-DBI >= 1.21
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	unixODBC-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD::ODBC is DBD module interfacing the ODBC databases.

%description -l pl.UTF-8
DBD::ODBC jest modułem DBD komunikującym się z bazami danych z użyciem
ODBC.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%{__perl} -pi -e 's/.*(@\$\(NOOP\))/\t$1/' Makefile.PL
%{__perl} -pi -e 's@/lib/libodbc@/%{_lib}/libodbc@' Makefile.PL

%build
%{__perl} Makefile.PL \
	-o /usr \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{?with_tests:%{__make} test}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/DBD/ODBC.pm
%{perl_vendorarch}/DBD/ODBC
%dir %{perl_vendorarch}/auto/DBD/ODBC
%{perl_vendorarch}/auto/DBD/ODBC/ODBC.bs
%attr(755,root,root) %{perl_vendorarch}/auto/DBD/ODBC/ODBC.so
%{_mandir}/man3/*
