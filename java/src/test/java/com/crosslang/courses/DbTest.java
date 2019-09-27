package com.crosslang.courses;

import org.junit.Test;

public class DbTest {

	@Test
	public void test() {
		Db test = new Db();
		NGram n1 = new Unigram("Hello");
		NGram n2 = new BiGram("Hello World");
		Sentence s1 = new Sentence();
		s1.addNgram(n1);
		Sentence s2 = new Sentence();
		s2.addNgram(n2);
		test.addSentence(s1);
		test.addSentence(s2);
		test.printSentenceNGrams();
	}

}
