"""Run a synthetic offline audit through the real report pipeline."""
from unittest.mock import patch
import audit_site


def build_demo():
    def fixture_fetch(url, timeout, max_bytes=None):
        if url == "https://demo.example":
            return ("<html><title>Offline fixture</title><body>Demo</body></html>",
                    {"content-type": "text/html"}, 200, url, None)
        return (None, {}, 404, url, "Synthetic fixture: endpoint absent")

    # No fallback to real transport, including for endpoint and script checks.
    with patch.object(audit_site, "fetch_url", side_effect=fixture_fetch):
        report = audit_site.build_report("https://demo.example", 1)
    report.scanned_at = "2026-10-17T00:00:00+00:00"
    report.notes.insert(0, "SYNTHETIC OFFLINE DEMO. No website was contacted. Missing headers are review indicators, not proof of exploitation.")
    return report


if __name__ == "__main__":
    print(audit_site.render_markdown(build_demo()))
