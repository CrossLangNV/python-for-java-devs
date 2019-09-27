package com.crosslang.courses;

import java.util.ArrayList;
import java.util.List;
import lombok.extern.slf4j.Slf4j;

@Slf4j
public class Db {

	private List<Sentence> sentences;

	public Db() {
		this.sentences = new ArrayList<Sentence>();
	}
	
	public void addSentence(Sentence sentence) {
		this.sentences.add(sentence);
	}
	
	public List<Sentence> getSentences() {
		return sentences;
	}

	public void printSentenceNGrams() {
		for (Sentence sentence : sentences) {
			for (NGram ngram : sentence.getNGrams()) {
				log.info(Integer.toString(ngram.getOrder()) + ": " + ngram.toString());
			}
		}
	}

}
