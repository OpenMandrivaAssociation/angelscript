%define major	23600
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname %{name} -d

%global _vpath_srcdir	sdk/%{name}/projects/meson/

Name:		angelscript
Version:	2.36.0
Release:	1
Summary:	Scripting library
License:	zlib
Group:		System/Libraries
URL:		https://www.angelcode.com/angelscript/
Source0:	http://www.angelcode.com/angelscript/sdk/files/%{name}_%{version}.zip

BuildRequires:	meson

%description
The AngelCode Scripting Library, or AngelScript as it is also known,
is a scripting library designed to allow applications to extend their
functionality through external scripts.

It supports Unix sockets and TCP/IP sockets with optional
SSL/TLS support.

%package -n	%{libname}
Summary:	Scripting library
Group:		System/Libraries

%description -n %{libname}
The AngelCode Scripting Library, or AngelScript as it is also known,
is a scripting library designed to allow applications to extend their
functionality through external scripts.

It supports Unix sockets and TCP/IP sockets with optional
SSL/TLS support.

%package -n	%{devname}
Summary:	Development files for AngelScript
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
The AngelCode Scripting Library, or AngelScript as it is also known,
is a scripting library designed to allow applications to extend their
functionality through external scripts.

This subpackage contains libraries and header files for developing
applications that want to make use of the AngelScript library.

%prep
%setup -qc

%build
%meson
%meson_build

%install
%meson_install

%files
%doc sdk/docs/*

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}{,.*}

%files -n %{devname}
%{_includedir}/*.h
%{_libdir}/lib%{name}.so
