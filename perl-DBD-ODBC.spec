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
Version:	1.60
Release:	1
# GPL or Artistic as specified in perl README file
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DBD/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e9a2bec96744f960832e4f47f9e4bcd0
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

%build
# pass PERL_MM_USE_DEFAULT to avoid threads warning prompt
PERL_MM_USE_DEFAULT=1 \
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
%attr(755,root,root) %{perl_vendorarch}/auto/DBD/ODBC/ODBC.so
%{_mandir}/man3/DBD::ODBC.3pm*
