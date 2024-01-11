Name:                   libconfig
Summary:                C/C++ configuration file library
Version:                1.5
Release:                9%{?dist}
License:                LGPLv2+
Group:                  System Environment/Libraries
Source0:                http://www.hyperrealm.com/libconfig/libconfig-%{version}.tar.gz
# Generated from libconfig 1.5 on Fedora 23 x86_64 (2015-12-17)
Source1:		libconfig.pdf
URL:                    http://www.hyperrealm.com/libconfig/
BuildRequires:          texinfo-tex, tex(ecbx1095.tfm), tex(ecrm1095.tfm), tex(cm-super-t1.enc)
BuildRequires:		bison, flex

%description
Libconfig is a simple library for manipulating structured configuration
files. This file format is more compact and more readable than XML. And
unlike XML, it is type-aware, so it is not necessary to do string parsing
in application code.

%package devel
Summary:                Development files for libconfig
Group:                  Development/Libraries
Requires:               %{name} = %{version}-%{release}
Requires:               pkgconfig
Requires(post):         /sbin/install-info
Requires(preun):        /sbin/install-info

%description devel
Development libraries and headers for developing software against
libconfig.

%prep
%setup -q
iconv -f iso-8859-1 -t utf-8 -o AUTHORS{.utf8,}
mv AUTHORS{.utf8,}

%build
%configure --disable-static
make %{?_smp_mflags}
make pdf

%install
make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_infodir}/dir
# Need to use a pre-built copy to support multilib
rm -rf doc/libconfig.pdf
install -p %{SOURCE1} doc/

%check
./tests/libconfig_tests

%ldconfig_scriptlets

%post devel
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :

%preun devel
if [ $1 = 0 ]; then
   /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi

%files
%doc AUTHORS ChangeLog COPYING.LIB README
%{_libdir}/libconfig*.so.*

%files devel
%doc doc/libconfig.pdf
%{_includedir}/libconfig*
%{_libdir}/libconfig*.so
%{_libdir}/pkgconfig/libconfig*.pc
%{_infodir}/libconfig.info*

%changelog
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5-8
- Switch to %%ldconfig_scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 17 2015 Tom Callaway <spot@fedoraproject.org> - 1.5-3
- fix pdf file by having a pre-generated pdf as source1 (bz 1292449)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 19 2015 Tom Callaway <spot@fedoraproject.org> - 1.5-1
- update to 1.5

* Thu Apr 16 2015 Dominik Mierzejewski <rpm@greysector.net> - 1.4.9-8
- rebuilt for gcc-5.0.0-0.22.fc23

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Sep  4 2013 Tom Callaway <spot@fedoraproject.org> - 1.4.9-5
- handle everything with doc

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Pavel Raiskup <praiskup@redhat.com> - 1.4.9-3
- enable simple upstream test-suite during check phase

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct  1 2012 Tom Callaway <spot@fedoraproject.org> - 1.4.9-1
- update to 1.4.9

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Aug 12 2011 Tom Callaway <spot@fedoraproject.org> - 1.4.8-1
- update to 1.4.8

* Wed Mar 23 2011 Tom Callaway <spot@fedoraproject.org> - 1.4.7-1
- update to 1.4.7

* Tue Mar  1 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4.6-1
- Update to 1.4.6
- Install libconfig_tests
- Fix rpmlint warnings

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed May  5 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.4.5-1
- update to 1.4.5

* Wed Aug 19 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.3.2-1
- update to 1.3.2

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.3.1-2
- prevent multilib conflicts with the generated pdf

* Fri Sep 12 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.3.1-1
- update to 1.3.1

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.1-2
- Autorebuild for GCC 4.3

* Tue Feb 19 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.1-1
- bump to 1.2.1

* Fri Nov 30 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.2-4
- nuke %%{_infodir}/dir, we handle it in %%post

* Fri Nov 30 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.2-3
- move all docs to devel
- move scriptlets around to match
- move requires around to match

* Fri Nov 30 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.2-2
- BR: texinfo-tex (not Requires)

* Fri Nov 30 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.2-1
- Initial package for Fedora
