#
# Conditional build:
%bcond_with	internal_fuse	# build with internal libfuse
#
Summary:	The NTFS driver with read and write support
Summary(pl.UTF-8):	Sterownik do NTFS umożliwiający odczyt i zapis
Name:		ntfs-3g_ntfsprogs
Version:	2011.4.12
Release:	3
Epoch:		1
License:	GPL v2+
Group:		Applications/System
#Source0-Download: http://www.tuxera.com/community/ntfs-3g-download/
Source0:	http://www.tuxera.com/opensource/%{name}-%{version}.tgz
# Source0-md5:	9c4ce318373b15332239a77a9d2a39fe
Source1:	%{name}.rules
URL:		http://www.tuxera.com/community/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
%{!?with_internal_fuse:BuildRequires:	libfuse-devel >= 2.6.0}
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
ntfs-3g_ntfsprogs is a stable, full-featured, read-write NTFS driver
for Linux, Android, Mac OS X, FreeBSD, NetBSD, OpenSolaris, QNX,
Haiku, and other operating systems. It provides safe handling of the
Windows XP, Windows Server 2003, Windows 2000, Windows Vista, Windows
Server 2008 and Windows 7 NTFS file systems.

%package -n ntfsprogs
Summary:	The NTFS driver with read and write support
Summary(pl.UTF-8):	Sterownik do NTFS umożliwiający odczyt i zapis
Group:		Applications/System

%description -n ntfsprogs
The driver to NTFS with read and write support. It is able to
unlimited and fully save file creation and deletion.

This package contains the following utilities:

- ntfsfix - attempt to fix an NTFS partition that has been damaged by
  the Linux NTFS driver. It should be run every time after you have
  used the Linux NTFS driver to write to an NTFS partition to prevent
  massive data corruption from happening when Windows mounts the
  partition.

  IMPORTANT: Run this only *after* unmounting the partition in Linux
  but *before* rebooting into Windows NT/2000!,
- mkntfs - create partition with the NTFS filesystem,
- ntfslabel - display/change the label of an NTFS partition,
- ntfsundelete - recover deleted files from an NTFS volume,
- ntfsresize - resize an NTFS volume,
- ntfsclone - clone, image, restore or rescue NTFS,
- ntfswipe - wipe junk from unused space,
- ntfsdecrypt - descrypt $EFS-encrypted files.

You can find more information about these utilities in their manuals.

%description -n ntfsprogs -l pl.UTF-8
Sterownik do systemu plików NTFS posiadający możliwość zarówno odczytu
jak i zapisu. Umożliwia tworzenie i kasowanie plików nieograniczoną
liczbę razy.

Pakiet zawiera następujące narzędzia:

- ntfsfix - próbuje naprawiać partycję NTFS uszkodzone przez linuksowy
  sterownik do NTFS. Powinien być uruchamiany po każdym zapisie na
  partycji NTFS, aby zapobiec masowemu zniszczeniu danych.

  WAŻNE: należy uruchamiać ten program tylko *po* odmontowaniu
  partycji pod Linuksem, ale *przed* uruchomieniem Windows NT/2000!
- mkntfs - "formatuje" partycję NTFS.
- ntfslabel - wyświetla/zmienia etykietę partycji NTFS.
- ntfsundelete - odzyskuje usunięte pliki z wolumenu NTFS.
- ntfsresize - zmienia rozmiar wolumenu NTFS.
- ntfsclone
- ntfswipe
- ntfsdecrypt

Więcej informacji na temat tych narzędzi można znaleźć w manualach.

%package -n ntfs-3g
Summary:	The NTFS driver with read and write support
Summary(pl.UTF-8):	Sterownik do NTFS umożliwiający odczyt i zapis
Group:		Applications/System
Obsoletes:	ntfsprogs-fuse

%description -n ntfs-3g
The driver to NTFS with read and write support. It is able to
unlimited and fully save file creation and deletion.

%description -n ntfs-3g -l pl.UTF-8
Sterownik do systemu plików NTFS posiadający możliwość zarówno odczytu
jak i zapisu. Umożliwia tworzenie i kasowanie plików nieograniczoną
liczbę razy.

%package -n ntfs-3g-libs
Summary:	ntfs-3g shared libraries
Summary(pl.UTF-8):	Wspólne biblioteki ntfs-3g
Group:		Libraries

%description -n ntfs-3g-libs
ntfs-3g shared libraries.

%description -n ntfs-3g-libs -l pl.UTF-8
Współdzielone biblioteki ntfs-3g.

%package -n ntfs-3g-devel
Summary:	Header files for libntfs-3g library
Summary(pl.UTF-8):	Pliki nagłówkowe dla biblioteki libntfs-3g
Group:		Development/Libraries
Requires:	ntfs-3g-libs = %{epoch}:%{version}-%{release}
Obsoletes:	ntfsprogs-devel

%description -n ntfs-3g-devel
This package includes the header files needed to link software with
libnfts-3g libraries.

%description -n ntfs-3g-devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do budowania programów korzystających z
bibliotek libntfs-3g.

%package -n ntfs-3g-static
Summary:	Static version of libntfs-3g library
Summary(pl.UTF-8):	Statyczna wersja bibliotek libntfs-3g
Group:		Development/Libraries
Requires:	ntfs-3g-devel = %{epoch}:%{version}-%{release}

%description -n ntfs-3g-static
This package contains the static version of libntfs-3g library.

%description -n ntfs-3g-static -l pl.UTF-8
Ten pakiet zawiera statyczną wersję bibliotek libntfs-3g.

%package -n ntfs-3g-udev
Summary:	udev integration for ntfs-3g
Summary(pl.UTF-8):	Integracja ntfs-3g z udevem
Group:		Applications/System
Requires:	ntfs-3g = %{epoch}:%{version}-%{release}
Obsoletes:	ntfs-3g-hal

%description -n ntfs-3g-udev
udev integration for ntfs-3g.

%description -n ntfs-3g-udev -l pl.UTF-8
Integracja ntfs-3g z udevem.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}

%configure \
	--disable-ldconfig \
	--with-fuse=%{?with_internal_fuse:in}%{!?with_internal_fuse:ex}ternal

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/udev/rules.d
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# mount.ntfs-3g manpage fix
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man8/mount.ntfs-3g.8
echo ".so ntfs-3g.8" > $RPM_BUILD_ROOT%{_mandir}/man8/mount.ntfs-3g.8

install %{SOURCE1} $RPM_BUILD_ROOT/lib/udev/rules.d/99-ntfs3g.rules

# Symlink to allow automount using ntfs-3g:
ln -sf %{_bindir}/ntfs-3g $RPM_BUILD_ROOT%{_sbindir}/mount.ntfs

%clean
rm -rf $RPM_BUILD_ROOT

%post -n ntfs-3g-libs -p /sbin/ldconfig
%postun -n ntfs-3g-libs -p /sbin/ldconfig

%files -n ntfsprogs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ntfscat
%attr(755,root,root) %{_bindir}/ntfscluster
%attr(755,root,root) %{_bindir}/ntfscmp
%attr(755,root,root) %{_bindir}/ntfsfix
%attr(755,root,root) %{_bindir}/ntfsinfo
%attr(755,root,root) %{_bindir}/ntfsls
%attr(755,root,root) %{_sbindir}/mkntfs
%attr(755,root,root) %{_sbindir}/ntfsclone
%attr(755,root,root) %{_sbindir}/ntfscp
%attr(755,root,root) %{_sbindir}/ntfslabel
%attr(755,root,root) %{_sbindir}/ntfsresize
%attr(755,root,root) %{_sbindir}/ntfsundelete
%attr(755,root,root) /sbin/mkfs.ntfs
%{_mandir}/man8/mkfs.ntfs.8*
%{_mandir}/man8/mkntfs.8*
%{_mandir}/man8/ntfscat.8*
%{_mandir}/man8/ntfsclone.8*
%{_mandir}/man8/ntfscluster.8*
%{_mandir}/man8/ntfscmp.8*
%{_mandir}/man8/ntfscp.8*
%{_mandir}/man8/ntfsfix.8*
%{_mandir}/man8/ntfsinfo.8*
%{_mandir}/man8/ntfslabel.8*
%{_mandir}/man8/ntfsls.8*
%{_mandir}/man8/ntfsprogs.8*
%{_mandir}/man8/ntfsresize.8*
%{_mandir}/man8/ntfsundelete.8*

%files -n ntfs-3g
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/lowntfs-3g
%attr(755,root,root) %{_bindir}/ntfs-3g
%attr(755,root,root) %{_bindir}/ntfs-3g.probe
%attr(755,root,root) %{_bindir}/ntfs-3g.secaudit
%attr(755,root,root) %{_bindir}/ntfs-3g.usermap
%attr(755,root,root) %{_sbindir}/mount.lowntfs-3g
%attr(755,root,root) %{_sbindir}/mount.ntfs
%attr(755,root,root) %{_sbindir}/mount.ntfs-3g
%{_mandir}/man8/mount.lowntfs-3g.8*
%{_mandir}/man8/mount.ntfs-3g.8*
%{_mandir}/man8/ntfs-3g.8*
%{_mandir}/man8/ntfs-3g.probe.8*
%{_mandir}/man8/ntfs-3g.secaudit.8*
%{_mandir}/man8/ntfs-3g.usermap.8*

%files -n ntfs-3g-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libntfs-3g.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libntfs-3g.so.81

%files -n ntfs-3g-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libntfs-3g.so
%{_libdir}/libntfs-3g.la
%{_includedir}/ntfs-3g
%{_pkgconfigdir}/libntfs-3g.pc

%files -n ntfs-3g-static
%defattr(644,root,root,755)
%{_libdir}/libntfs-3g.a

%files -n ntfs-3g-udev
%defattr(644,root,root,755)
/lib/udev/rules.d/99-ntfs3g.rules
