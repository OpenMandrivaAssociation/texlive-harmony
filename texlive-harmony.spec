# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/harmony
# catalog-date 2009-06-25 00:34:53 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-harmony
Version:	20180303
Release:	2
Summary:	Typeset harmony symbols, etc., for musicology
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/harmony
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/harmony.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/harmony.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package harmony.sty uses the packages ifthen and amssymb
from the amsfonts bundle, together with the LaTeX font
lcirclew10 and the font musix13 from musixtex.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/harmony/harmony.sty
%doc %{_texmfdistdir}/doc/latex/harmony/README
%doc %{_texmfdistdir}/doc/latex/harmony/harmony.pdf
%doc %{_texmfdistdir}/doc/latex/harmony/harmony.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090625-2
+ Revision: 752463
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20090625-1
+ Revision: 718601
- texlive-harmony
- texlive-harmony
- texlive-harmony
- texlive-harmony

