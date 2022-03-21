import pytest
from src.TRIES.suffix_trie.suffix_trie import SuffixTrie

test_cases = [("babc",
    {
    "methodCallResults": [
        {
        "arguments": ["abc"],
        "method": "contains",
        "output": True
        }]}
    ,
    { "trie": {
        "a": {
            "b": {
                "c": {
                "*": True
                }
            }
        },
        "b": {
            "a": {
                "b": {
                "c": {
                    "*": True
                }
                }
            },
        "c": {
            "*": True
        }
        },
        "c": {
            "*": True
        }
    }
    }
)]

@pytest.mark.parametrize("string, method_call_results, trie", test_cases)
def test_suffix_trie_construction(string, method_call_results, trie):
    suffix_trie = SuffixTrie(string)
    assert suffix_trie.root == trie["trie"]
    for call_result in method_call_results["methodCallResults"]:
        method_to_call = getattr(suffix_trie, call_result["method"])
        argument = call_result["arguments"][0]
        output = call_result["output"]
        assert method_to_call(argument) == output