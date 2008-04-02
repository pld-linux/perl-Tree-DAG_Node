#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Tree
%define		pnam	DAG_Node
Summary:	Tree::DAG_Node - (super)class for representing nodes in a tree
Summary(pl.UTF-8):	Tree::DAG_Node - (nad)klasa do reprezentowania węzłów w drzewie
Name:		perl-Tree-DAG_Node
Version:	1.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Tree/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3b006f128bd1d8961fc57c466ffa05f2
URL:		http://search.cpan.org/dist/Tree-DAG_Node/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class encapsulates/makes/manipulates objects that represent nodes
in a tree structure. The tree structure is not an object itself, but
is emergent from the linkages you create between nodes. This class
provides the methods for making linkages that can be used to build up
a tree, while preventing you from ever making any kinds of linkages
which are not allowed in a tree (such as having a node be its own
mother or ancestor, or having a node have two mothers).

%description -l pl.UTF-8
Ta klasa obudowuje, tworzy i obrabia obiekty, które reprezentują węzły
w strukturze drzewiastej. Struktura drzewiasta jako taka nie jest
obiektem, ale wyłania się z połączeń tworzonych pomiędzy węzłami. Ta
klasa udostępnia metody do tworzenia połączeń, które mogą być używane
do zbudowania drzewa, nie dopuszczając na zrobienie połączeń nie
dozwolonych w drzewie (takich jak połączenie węzła z jego przodkiem,
lub nadanie węzłowi dwóch przodków).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Tree/DAG_Node.pm
%{_mandir}/man3/*
