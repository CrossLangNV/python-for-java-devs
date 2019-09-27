package com.crosslang.courses;

public class Unigram implements NGram {

	private String text;
	
	public Unigram(String text) {
		this.text = text;
	}
	
	@Override
	public int getOrder() {
		return 1;
	}

	@Override
	public String getText() {
		return this.text;
	}
	
	@Override
	public String toString() {
		return "unigram" + this.text ;
	}
}
