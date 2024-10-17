%define api     1.0
%define oname   gstreamer%{api}

Name: %{oname}-plugins-espeak
Version: 0.4.0
Release: 2
Summary: A simple gstreamer plugin to use espeak

Group: System/Libraries
License: LGPLv2+
URL: https://wiki.sugarlabs.org/go/Activity_Team/gst-plugins-espeak
Source0: http://download.sugarlabs.org/sources/honey/gst-plugins-espeak/gst-plugins-espeak-%{version}.tar.gz

BuildRequires: espeak-devel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0) 
BuildRequires: gstreamer1.0-devel

%description
A simple gstreamer plugin to use espeak as a sound source.
It was developed to simplify the espeak usage in the Sugar Speak activity.
The plugin uses given text to produce audio output.

%prep
%setup -q  -n gst-plugins-espeak-%{version}


%build
# make sure to build the plugin for release
sed -i 's/NANO=1/NANO=0/g' configure
%configure
%make


%install
%makeinstall_std

# remove libtool archives
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%doc AUTHORS COPYING README NEWS
%{_libdir}/gstreamer-1.0/libgstespeak.so

