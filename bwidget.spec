#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bwidget
Version  : 1.9.13
Release  : 4
URL      : https://sourceforge.net/projects/tcllib/files/BWidget/1.9.13/bwidget-1.9.13.tar.gz
Source0  : https://sourceforge.net/projects/tcllib/files/BWidget/1.9.13/bwidget-1.9.13.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : TCL
Requires: bwidget-license = %{version}-%{release}
Patch1: build.patch

%description
BWidget ToolKit 1.9.0				July 2009
See the file LICENSE.txt for license info (uses Tcl's BSD-style license).

%package license
Summary: license components for the bwidget package.
Group: Default

%description license
license components for the bwidget package.


%prep
%setup -q -n bwidget-1.9.13
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545509488
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1545509488
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bwidget
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/bwidget/LICENSE.txt
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/bwidget/BWman/ArrowButton.html
/usr/lib64/bwidget/BWman/BWidget.html
/usr/lib64/bwidget/BWman/Button.html
/usr/lib64/bwidget/BWman/ButtonBox.html
/usr/lib64/bwidget/BWman/ComboBox.html
/usr/lib64/bwidget/BWman/Dialog.html
/usr/lib64/bwidget/BWman/DragSite.html
/usr/lib64/bwidget/BWman/DropSite.html
/usr/lib64/bwidget/BWman/DynamicHelp.html
/usr/lib64/bwidget/BWman/Entry.html
/usr/lib64/bwidget/BWman/Label.html
/usr/lib64/bwidget/BWman/LabelEntry.html
/usr/lib64/bwidget/BWman/LabelFrame.html
/usr/lib64/bwidget/BWman/ListBox.html
/usr/lib64/bwidget/BWman/MainFrame.html
/usr/lib64/bwidget/BWman/MessageDlg.html
/usr/lib64/bwidget/BWman/NoteBook.html
/usr/lib64/bwidget/BWman/PagesManager.html
/usr/lib64/bwidget/BWman/PanedWindow.html
/usr/lib64/bwidget/BWman/PanelFrame.html
/usr/lib64/bwidget/BWman/PasswdDlg.html
/usr/lib64/bwidget/BWman/ProgressBar.html
/usr/lib64/bwidget/BWman/ProgressDlg.html
/usr/lib64/bwidget/BWman/ScrollView.html
/usr/lib64/bwidget/BWman/ScrollableFrame.html
/usr/lib64/bwidget/BWman/ScrolledWindow.html
/usr/lib64/bwidget/BWman/SelectColor.html
/usr/lib64/bwidget/BWman/SelectFont.html
/usr/lib64/bwidget/BWman/Separator.html
/usr/lib64/bwidget/BWman/SpinBox.html
/usr/lib64/bwidget/BWman/StatusBar.html
/usr/lib64/bwidget/BWman/TitleFrame.html
/usr/lib64/bwidget/BWman/Tree.html
/usr/lib64/bwidget/BWman/Widget.html
/usr/lib64/bwidget/BWman/contents.html
/usr/lib64/bwidget/BWman/index.html
/usr/lib64/bwidget/BWman/navtree.html
/usr/lib64/bwidget/BWman/options.htm
/usr/lib64/bwidget/CHANGES.txt
/usr/lib64/bwidget/ChangeLog
/usr/lib64/bwidget/LICENSE.txt
/usr/lib64/bwidget/Makefile
/usr/lib64/bwidget/README.txt
/usr/lib64/bwidget/arrow.tcl
/usr/lib64/bwidget/bitmap.tcl
/usr/lib64/bwidget/button.tcl
/usr/lib64/bwidget/buttonbox.tcl
/usr/lib64/bwidget/color.tcl
/usr/lib64/bwidget/combobox.tcl
/usr/lib64/bwidget/demo/basic.tcl
/usr/lib64/bwidget/demo/bwidget.xbm
/usr/lib64/bwidget/demo/demo.tcl
/usr/lib64/bwidget/demo/dnd.tcl
/usr/lib64/bwidget/demo/manager.tcl
/usr/lib64/bwidget/demo/select.tcl
/usr/lib64/bwidget/demo/tmpldlg.tcl
/usr/lib64/bwidget/demo/tree.tcl
/usr/lib64/bwidget/demo/x1.xbm
/usr/lib64/bwidget/dialog.tcl
/usr/lib64/bwidget/dragsite.tcl
/usr/lib64/bwidget/dropsite.tcl
/usr/lib64/bwidget/dynhelp.tcl
/usr/lib64/bwidget/entry.tcl
/usr/lib64/bwidget/font.tcl
/usr/lib64/bwidget/images/bold.gif
/usr/lib64/bwidget/images/copy.gif
/usr/lib64/bwidget/images/cut.gif
/usr/lib64/bwidget/images/dragfile.gif
/usr/lib64/bwidget/images/dragicon.gif
/usr/lib64/bwidget/images/error.gif
/usr/lib64/bwidget/images/file.gif
/usr/lib64/bwidget/images/folder.gif
/usr/lib64/bwidget/images/hourglass.gif
/usr/lib64/bwidget/images/info.gif
/usr/lib64/bwidget/images/italic.gif
/usr/lib64/bwidget/images/minus.xbm
/usr/lib64/bwidget/images/new.gif
/usr/lib64/bwidget/images/opcopy.xbm
/usr/lib64/bwidget/images/open.gif
/usr/lib64/bwidget/images/openfold.gif
/usr/lib64/bwidget/images/oplink.xbm
/usr/lib64/bwidget/images/opmove.xbm
/usr/lib64/bwidget/images/overstrike.gif
/usr/lib64/bwidget/images/palette.gif
/usr/lib64/bwidget/images/passwd.gif
/usr/lib64/bwidget/images/paste.gif
/usr/lib64/bwidget/images/plus.xbm
/usr/lib64/bwidget/images/print.gif
/usr/lib64/bwidget/images/question.gif
/usr/lib64/bwidget/images/redo.gif
/usr/lib64/bwidget/images/save.gif
/usr/lib64/bwidget/images/target.xbm
/usr/lib64/bwidget/images/underline.gif
/usr/lib64/bwidget/images/undo.gif
/usr/lib64/bwidget/images/warning.gif
/usr/lib64/bwidget/init.tcl
/usr/lib64/bwidget/label.tcl
/usr/lib64/bwidget/labelentry.tcl
/usr/lib64/bwidget/labelframe.tcl
/usr/lib64/bwidget/lang/da.rc
/usr/lib64/bwidget/lang/de.rc
/usr/lib64/bwidget/lang/en.rc
/usr/lib64/bwidget/lang/es.rc
/usr/lib64/bwidget/lang/fr.rc
/usr/lib64/bwidget/lang/hu.rc
/usr/lib64/bwidget/lang/nl.rc
/usr/lib64/bwidget/lang/no.rc
/usr/lib64/bwidget/lang/pl.rc
/usr/lib64/bwidget/listbox.tcl
/usr/lib64/bwidget/mainframe.tcl
/usr/lib64/bwidget/messagedlg.tcl
/usr/lib64/bwidget/notebook.tcl
/usr/lib64/bwidget/pagesmgr.tcl
/usr/lib64/bwidget/panedw.tcl
/usr/lib64/bwidget/panelframe.tcl
/usr/lib64/bwidget/passwddlg.tcl
/usr/lib64/bwidget/pkgIndex.tcl
/usr/lib64/bwidget/progressbar.tcl
/usr/lib64/bwidget/progressdlg.tcl
/usr/lib64/bwidget/scrollframe.tcl
/usr/lib64/bwidget/scrollview.tcl
/usr/lib64/bwidget/scrollw.tcl
/usr/lib64/bwidget/separator.tcl
/usr/lib64/bwidget/spinbox.tcl
/usr/lib64/bwidget/statusbar.tcl
/usr/lib64/bwidget/tests/entry.test
/usr/lib64/bwidget/titleframe.tcl
/usr/lib64/bwidget/tree.tcl
/usr/lib64/bwidget/utils.tcl
/usr/lib64/bwidget/widget.tcl
/usr/lib64/bwidget/wizard.tcl
/usr/lib64/bwidget/xpm2image.tcl

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bwidget/LICENSE.txt
