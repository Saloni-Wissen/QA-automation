from graph import test_graph
import os
import webbrowser


def main():
    result = test_graph.invoke({
        "retry_count": 0
    })

    print("\n=== QA PIPELINE RESULT ===\n")

    print(f"VERDICT        : {result.get('verdict')}")
    print(f"RETRY COUNT    : {result.get('retry_count', 0)}")

    if "coverage" in result:
        print(f"COVERAGE       : {result['coverage']}%")

    if result.get("coverage_summary"):
        print("\nCOVERAGE SUMMARY:")
        print(result["coverage_summary"])

    jacoco_html = result.get("jacoco_html")
    if jacoco_html:
        print(f"\nJACOCO REPORT  : {jacoco_html}")

        if os.path.exists(jacoco_html):
            webbrowser.open(f"file:///{jacoco_html}")


if __name__ == "__main__":
    main()
