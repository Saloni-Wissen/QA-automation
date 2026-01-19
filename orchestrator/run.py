from graph import test_graph

if __name__ == "__main__":
    result = test_graph.invoke({})

    print("\n=== FINAL VERDICT ===")
    for k, v in result.items():
        print(f"\n{k.upper()}:\n{v}")
