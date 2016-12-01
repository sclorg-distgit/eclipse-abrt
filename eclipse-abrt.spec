%{?scl:%scl_package eclipse-abrt}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

%global baserelease 2

Name:		%{?scl_prefix}eclipse-abrt
Version:	0.0.3
Release:	1.%{baserelease}%{?dist}
Summary:	Eclipse ABRT plugin
License:	EPL
URL:		https://pagure.io/eclipse-abrt

Source0:	https://pagure.io/releases/eclipse-abrt/eclipse-abrt-%{version}.tar.xz


BuildArch:	noarch

BuildRequires:	%{?scl_prefix}tycho
BuildRequires:	%{?scl_prefix}tycho-extras
BuildRequires:	%{?scl_prefix}eclipse-platform
BuildRequires:	%{?scl_prefix}jnr-unixsocket
BuildRequires:	%{?scl_prefix}eclipse-epp-logging
BuildRequires:	%{?scl_prefix}eclipse-license
BuildRequires:	%{?scl_prefix}osgi(org.eclipse.mylyn.bugzilla.ui)

Requires:	%{?scl_prefix}eclipse-platform >= 1:4.3.2
Requires:	%{?scl_prefix}eclipse-epp-logging

Obsoletes:	%{?scl_prefix}eclipse-mylyn-fedora-integration >= 1.0.4-1

%description
This plugin provide support to add error reports from Eclipse to ABRT

%prep
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%setup -q -n eclipse-abrt-%{version}

rm pom.xml
xmvn -o org.eclipse.tycho:tycho-pomgenerator-plugin:generate-poms \
  -DgroupId=org.fedoraproject.abrt -Dversion=%{version}-SNAPSHOT
%{?scl:EOF}


%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%mvn_build  -j -- -f pom.xml
%{?scl:EOF}


%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%mvn_install
%{?scl:EOF}


%files -f .mfiles

%changelog
* Tue Aug 02 2016 Mat Booth <mat.booth@redhat.com> - 0.0.3-1.2
- Generate poms

* Tue Aug 02 2016 Mat Booth <mat.booth@redhat.com> - 0.0.3-1.1
- Auto SCL-ise package for rh-eclipse46 collection

* Wed Jun 8 2016 Alexander Kurtakov <akurtako@redhat.com> 0.0.3-1
- Update to upstream 0.0.3 release which obsoletes eclipse-mylyn-fedora-integration.

* Wed Apr 20 2016 Alexander Kurtakov <akurtako@redhat.com> 0.0.2-1
- Update to upstream 0.0.2 release.

* Thu Mar 24 2016 Sopot Cela <scela@redhat.com> - 0.0.1-1
- Initial upload
