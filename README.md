# bongard

Evaluating Claude models on [Bongard problems](https://en.wikipedia.org/wiki/Bongard_problem). The problems are drawn from the [Online Encyclopaedia of Bongard Problems](https://oebp.org/).

You can visualize results in the Streamlit app [here](https://bongard.streamlit.app/).

## Next steps

- Investigate model descriptions of abstract images, independent of the Bongard task. Indeed, this currently seems to be the bottleneck, not the abstract reasoning aspects.
- Add an LLM evaluation of model responses: give an LLM the solution and a model response, and ask it to determine whether the response is correct
- Evaluate more models than Haiku and Opus (including future releases targeting diagrams)
- Do more prompt engineering to 
- Evaluate via classification rather than description (that is, given 5 left images and 5 right images, place a new image in the correct group)

## Resources

As far as I can tell, no one has evaluated modern multimodal models on this exact task, but there is some related work:
- [On the Measure of Intelligence](https://arxiv.org/abs/1911.01547), which introduces the [Abstraction and Reasoning Corpus (ARC)](https://github.com/fchollet/ARC)
- [Bongard-LOGO: A New Benchmark for Human-Level Concept Learning and Reasoning](https://arxiv.org/abs/2010.00763)
- [Bongard-OpenWorld: Few-Shot Reasoning for Free-Form Visual Concepts in the Real World](https://openreview.net/pdf?id=hWS4MueyzC)
- [Neural networks for abstraction and reasoning: Towards broad generalization in machines](https://arxiv.org/abs/2402.03507v1)
- [Using Program Synthesis and Inductive Logic Programming to solve Bongard Problems](https://arxiv.org/abs/2110.09947), which uses [Dreamcoder](https://arxiv.org/abs/2006.08381)
- [D5](https://github.com/ruiqi-zhong/D5), which does something similar for text


Resources on Bongard problems:
- David Chapman, [A first lesson in meta-rationality](https://metarationality.com/bongard-meta-rationality)
- [Online Encyclopaedia of Bongard Problems](https://oebp.org/)
- [Henry Foundalis' index](https://www.foundalis.com/res/bps/bpidx.htm)