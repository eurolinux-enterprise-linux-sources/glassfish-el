%global artifactId javax.el

Name:           glassfish-el
Version:        2.2.5
Release:        6%{?dist}
Summary:        J2EE Expression Language Implementation
Group:          Development/Libraries
License:        CDDL or GPLv2 with exceptions
URL:            http://uel.java.net
# svn export https://svn.java.net/svn/uel~svn/tags/javax.el-2.2.5/ javax.el-2.2.5
# tar cvJf javax.el-2.2.5.tar.xz javax.el-2.2.5/
Source0:        %{artifactId}-%{version}.tar.xz
Source1:        generate_tarball.sh
BuildArch:      noarch

BuildRequires:  jvnet-parent
BuildRequires:  maven-local
BuildRequires:  maven
BuildRequires:  maven-source-plugin
BuildRequires:  mvn(javax.el:javax.el-api)

%description
This project provides an implementation of the Expression Language (EL).
The main goals are:
 * Improves current implementation: bug fixes and performance improvements
 * Provides API for use by other tools, such as Netbeans

%package javadoc
Group:          Documentation
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{artifactId}-%{version}

%mvn_file : %{name}
%mvn_alias : "org.eclipse.jetty.orbit:com.sun.el"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.2.5-6
- Mass rebuild 2013-12-27

* Thu Aug 22 2013 Michal Srb <msrb@redhat.com> - 2.2.5-5
- Migrate away from mvn-rpmbuild (Resolves: #997471)

* Fri Aug 02 2013 Michal Srb <msrb@redhat.com> - 2.2.5-4
- Add generate_tarball.sh script to SRPM

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.5-3
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Wed Mar  6 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.5-2
- Add depmap for org.eclipse.jetty.orbit
- Resolves: rhbz#918514

* Fri Feb 1 2013 David Xie <david.scriptfan@gmail.com> - 2.2.5-1
- Initial version of package
