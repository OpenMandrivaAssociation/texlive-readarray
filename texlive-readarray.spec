Name:		texlive-readarray
Version:	60540
Release:	2
Summary:	Read, store and recall array-formatted data
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/readarray
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/readarray.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/readarray.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows the user to input formatted data into
elements of a 2-D or 3-D array and to recall that data at will
by individual cell number. The data can be but need not be
numerical in nature. It can be, for example, formatted text.
While the package can be used for any application where indexed
data is called for, the package proves particularly useful when
elements of multiple arrays must be recallable and dynamically
combined at time of compilation, rather than in advance.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/readarray/readarray.sty
%doc %{_texmfdistdir}/doc/latex/readarray/README
%doc %{_texmfdistdir}/doc/latex/readarray/readarray.pdf
%doc %{_texmfdistdir}/doc/latex/readarray/readarray.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
