import pytest

from assignment_cl.commit_url_wrappers import (
    ALL_COMMIT_URL_WRAPPERS,
    FfmpegCommitUrl,
    FreedesktopCommitUrl,
    GitHubCommitUrl,
    GitLabCommitUrl,
    GlusterCommitUrl,
    GnuSavannahCommitUrl,
    OpensslCommitUrl,
    PostgresqlCommitUrl,
    QtCommitUrl,
    SourcewareCommitUrl,
)


@pytest.mark.parametrize(
    "commit_url_wrapper_factory,commit_url,base_url,account,project,commit_hash,repo_url",
    [
        # FfmpegCommitUrl
        (
            FfmpegCommitUrl,
            "https://git.ffmpeg.org/gitweb/mplayer.git/commit/33d9295663c37a37216633d7e3f07e7155da6144",
            "https://git.ffmpeg.org",
            None,
            "mplayer",
            "33d9295663c37a37216633d7e3f07e7155da6144",
            "https://git.ffmpeg.org/mplayer.git",
        ),
        (
            FfmpegCommitUrl,
            "http://git.ffmpeg.org/gitweb/fateserver.git/commit/fd02ae530d5fa5b71987a47125ff308633e98b76",
            "http://git.ffmpeg.org",
            None,
            "fateserver",
            "fd02ae530d5fa5b71987a47125ff308633e98b76",
            "http://git.ffmpeg.org/fateserver.git",
        ),
        # FreedesktopCommitUrl
        (
            FreedesktopCommitUrl,
            "https://cgit.freedesktop.org/libreoffice/core/commit/?id=5e8f64e50f97d39e83a3358697be14db03566878",
            "https://cgit.freedesktop.org",
            "libreoffice",
            "core",
            "5e8f64e50f97d39e83a3358697be14db03566878",
            "https://anongit.freedesktop.org/git/libreoffice/core.git",
        ),
        (
            FreedesktopCommitUrl,
            "https://cgit.freedesktop.org/exempi/commit/?id=886cd1d2314755adb1f4cdb99c16ff00830f0331",
            "https://cgit.freedesktop.org",
            None,
            "exempi",
            "886cd1d2314755adb1f4cdb99c16ff00830f0331",
            "https://anongit.freedesktop.org/git/exempi.git",
        ),
        # GitHubCommitUrl
        (
            GitHubCommitUrl,
            "https://github.com/systemd/systemd-stable/commit/572692f0bdd6a3fabe3dd4a3e8e5565cc69b5e14",
            "https://github.com",
            "systemd",
            "systemd-stable",
            "572692f0bdd6a3fabe3dd4a3e8e5565cc69b5e14",
            "https://github.com/systemd/systemd-stable.git",
        ),
        # GitLabCommitUrl
        (
            GitLabCommitUrl,
            "https://gitlab.com/libtiff/libtiff/-/commit/51558511bdbbcffdce534db21dbaf5d54b31638a",
            "https://gitlab.com",
            "libtiff",
            "libtiff",
            "51558511bdbbcffdce534db21dbaf5d54b31638a",
            "https://gitlab.com/libtiff/libtiff.git",
        ),
        (
            GitLabCommitUrl,
            "https://gitlab.isc.org/isc-projects/bind9/-/commit/0bbb0065e63c3231b320bd20d1121aed6c4d00d8",
            "https://gitlab.isc.org",
            "isc-projects",
            "bind9",
            "0bbb0065e63c3231b320bd20d1121aed6c4d00d8",
            "https://gitlab.isc.org/isc-projects/bind9.git",
        ),
        # GlusterCommitUrl
        (
            GlusterCommitUrl,
            "http://git.gluster.org/cgit/glusterfs.git/commit/?id=1f48d17fee0cac95648ec34d13f038b27ef5c6ac",
            "http://git.gluster.org",
            None,
            "glusterfs",
            "1f48d17fee0cac95648ec34d13f038b27ef5c6ac",
            "https://github.com/gluster/glusterfs.git",
        ),
        # GnuSavannahCommitUrl
        (
            GnuSavannahCommitUrl,
            "https://git.savannah.gnu.org/cgit/emacs/org-mode.git/commit/?id=8f8ec2ccf3f5ef8f38d68ec84a7e4739c45db485",
            "https://git.savannah.gnu.org",
            "emacs",
            "org-mode",
            "8f8ec2ccf3f5ef8f38d68ec84a7e4739c45db485",
            "https://git.savannah.gnu.org/git/emacs/org-mode.git",
        ),
        (
            GnuSavannahCommitUrl,
            "http://git.savannah.gnu.org/cgit/icoutils.git/commit/?id=bf97b99109607d4367a4e57df9a37cbcac02e220",
            "http://git.savannah.gnu.org",
            None,
            "icoutils",
            "bf97b99109607d4367a4e57df9a37cbcac02e220",
            "http://git.savannah.gnu.org/git/icoutils.git",
        ),
        # OpensslCommitUrl
        (
            OpensslCommitUrl,
            "https://git.openssl.org/gitweb/?p=openssl.git;a=commit;h=51e8a84ce742db0f6c70510d0159dad8f7825908",
            "https://git.openssl.org",
            None,
            "openssl",
            "51e8a84ce742db0f6c70510d0159dad8f7825908",
            "https://github.com/openssl/openssl.git",
        ),
        # PostgresqlCommitUrl
        (
            PostgresqlCommitUrl,
            "https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=2699fc035a75d0774c1f013e9320882287f78adb",
            "https://git.postgresql.org",
            None,
            "postgresql",
            "2699fc035a75d0774c1f013e9320882287f78adb",
            "https://git.postgresql.org/git/postgresql.git",
        ),
        # QtCommitUrl
        (
            QtCommitUrl,
            "https://code.qt.io/cgit/qt/qtbase.git/commit/?id=f432c08882ffebe5074ea28de871559a98a4d094",
            "https://code.qt.io",
            "qt",
            "qtbase",
            "f432c08882ffebe5074ea28de871559a98a4d094",
            "https://code.qt.io/qt/qtbase.git",
        ),
        # SourcewareCommitUrl
        (
            SourcewareCommitUrl,
            "https://sourceware.org/git/gitweb.cgi?p=binutils-gdb.git;h=d28fbc7197ba0e021a43f873eff90b05dcdcff6a",
            "https://sourceware.org",
            None,
            "binutils-gdb",
            "d28fbc7197ba0e021a43f873eff90b05dcdcff6a",
            "https://sourceware.org/git/binutils-gdb.git",
        ),
    ],
)
def test_commit_url_wrapper(
    commit_url_wrapper_factory,
    commit_url,
    base_url,
    account,
    project,
    commit_hash,
    repo_url,
):
    commit = commit_url_wrapper_factory.create_if_commit_url_acceptable(commit_url)
    assert commit.base_url == base_url
    assert commit.account == account
    assert commit.project_name == project
    assert commit.commit_hash == commit_hash
    assert commit.repo_url == repo_url


@pytest.mark.parametrize(
    "commit_url_wrapper_factory",
    [factory for factory in ALL_COMMIT_URL_WRAPPERS],
)
@pytest.mark.parametrize(
    "incorrect_commit_url",
    ["https://example.com/account/project.git/commit/33d9295663c37a37216633d7e3f07e7155da6144"],
)
def test_commit_url_wrapper_with_incorrect_commit_url(commit_url_wrapper_factory, incorrect_commit_url):
    commit = commit_url_wrapper_factory.create_if_commit_url_acceptable(incorrect_commit_url)
    assert commit is None
