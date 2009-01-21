Summary:	XML parsing for Tcl
Summary(pl.UTF-8):	Analizowanie XML-a dla Tcl-a
Name:		tclxml
Version:	3.2
Release:	1
License:	distributable
Group:		Development/Languages/Tcl
Source0:	http://dl.sourceforge.net/tclxml/%{name}-%{version}.tar.gz
# Source0-md5:	9d1605246c899eff7db591bca3c23200
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

%description -l pl.UTF-8
TclXML to API do analizy dokumentów XML przy użyciu języka skryptowego
Tcl. Jest to pakiet z kilkoma implementacjami analizatora. Celem
pakietu TclXML jest dostarczenie API dla skryptów Tcl pozwalającego na
implementowanie parserów "Plug-and-Play" - czyli aplikacja może używać
innych implementacji analizatora bez zmian w kodzie aplikacji.

%prep
%setup -q

%build
%configure \
%if %{_lib} == "lib64"
	--enable-64bit \
%endif
	--enable-threads
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README* doc/*.html
%{_includedir}/tclxml
%dir %{_libdir}/Tclxml*.*
%attr(755,root,root) %{_libdir}/Tclxml*.*/*.so
%{_libdir}/Tclxml*.*/*.a
%{_libdir}/Tclxml*.*/*.tcl
%dir %{_libdir}/*.sh
