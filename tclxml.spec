Summary:	XML parsing for Tcl
Summary(pl):	Analizowanie XML-a dla Tcl-a
Name:		tclxml
Version:	2.6
Release:	1
License:	distributable
Group:		Development/Languages/Tcl
Source0:	http://dl.sourceforge.net/tclxml/%{name}-%{version}.tar.gz
# Source0-md5:	a54d1d6965e2123529e80d2a7ed251ec
URL:		http://tclxml.sourceforge.net/tclxml.html
BuildRequires:	tcl-devel >= 8.4.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TclXML is an API for parsing XML documents using the Tcl scripting
language. It is also a package with several parser implementations.
The goal of the TclXML package is to provide an API for Tcl scripts
that allows "Plug-and-Play" parser implementations; ie. an application
will be able to use different parser implementations without change to
the application code.

%description -l pl
TclXML to API do analizy dokument�w XML przy u�yciu j�zyka skryptowego
Tcl. Jest to pakiet z kilkoma implementacjami analizatora. Celem
pakietu TclXML jest dostarczenie API dla skrypt�w Tcl pozwalaj�cego na
implementowanie parser�w "Plug-and-Play" - czyli aplikacja mo�e u�ywa�
innych implementacji analizatora bez zmian w kodzie aplikacji.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{makeinstall}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README doc/*.html
%{_includedir}/*.h
%dir %{_libdir}/Tclxml*.*
%attr(755,root,root) %dir %{_libdir}/Tclxml*.*/*.so
%{_libdir}/Tclxml*.*/*.tcl
%attr(755,root,root) %dir %{_libdir}/*.sh
