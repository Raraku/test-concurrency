from django_hosts import patterns, host
from .settings import ROOT_URLCONF

host_patterns = patterns(
    "", host(r"www", ROOT_URLCONF, name="www"), host(r"blog", "blog.urls", name="blog"),
)
