from pathlib import Path
import pytest
from slugify import slugify
import allure

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
  outcome = yield
  report = outcome.get_result()
  extra = getattr(report, "extra", [])

  if report.when == "call":
    xfail = hasattr(report, "wasxfail")
    is_failure = (report.failed and not xfail) or (report.skipped and xfail)

    if is_failure and "page" in item.funcargs:
      page = item.funcargs["page"]
      screenshot_dir = Path("screenshots")
      screenshot_dir.mkdir(exist_ok=True)
      screen_file = screenshot_dir / f"{slugify(item.nodeid)}.png"

      try:
        # Capture screenshot and get bytes
        screenshot_bytes = page.screenshot(path=str(screen_file))

        # Attach to Allure report under an explicit Step
        with allure.step("📷 Failure Screenshot Captured"):
          allure.attach(
            screenshot_bytes,
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
          )

      except Exception as e:
        print(f"\n[Warning] Failed to take/attach failure screenshot: {e}")

  report.extra = extra


