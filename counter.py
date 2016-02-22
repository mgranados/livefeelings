#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, json, re

file = open('tweets2.txt', 'r')
f=file.readlines()
file.close()

if (sys.argv[1] == "mex"):
    happywords = ["feliz", "felicidad", "bienestar", "alegria", "goce", "gozo", "dicha", "contento", "contenta"]
    sadwords = ["puta madre", "mierda", "chingada", "triste", "tristeza", "que mal", "nostalgia", "melancolía"]
    disgustwords = ["que asco", "fea", "feo", "gacho", "de la verga", "disgusto", "guacala"]
    surprisewords = ["que chido", "que chingon", "sorpresa", "sorprendido", "sorprendida"]
    angrywords = ["puta madre", "perra vida", "enojo", "enojada", "enojado", "pendejo", "pendeja", "me lleva la verga", "pendejadas"]
    fearwords = ["miedo", "no quiero", "culeando", "miedoso", "temor", "temeroso", "panico"]
else:
    happywords = ["happy", "awesome", "great", "exciting", "fun", "lol"]
    sadwords = ["sad", "sorrow", "unhappy",	"tragic", "unhappy", "unfortunate", "awful", "miserable", "wretched", "sorry", "pitiful", "pathetic", "traumatic", "heartbreaking"]
    disgustwords = ["disgust","disgusting","revulsion", "repugnance", "aversion", "distaste", "nausea", "abhorrence", "loathing", "detestation", "odium", "horror", "contempt", "outrage"]
    surprisewords = ["surprise", "shock", "bombshell", "revelation", "eye-opener", "wake-up call", "shocker"]
    angrywords = ["angry","anger", "irate", "mad", "annoyed", "cross", "vexed", "irritated", "indignant", "irked", "furious", "enraged", "infuriated", "incensed", "raging", "fuming", "seething", "choleric", "outraged",
    "livid", "apoplectic", "sore", "pissed off", "wrathful", "heated", "passionate", "stormy", "bad-tempered", "ill-tempered", "ill-natured", "acrimonious", "bitter"]
    fearwords = ["fear", "fearful","terror", "fright", "fearfulness", "horror", "alarm", "panic", "agitation", "trepidation", "dread", "consternation", "dismay", "distress", "anxiety", "worry", "angst", "unease", "uneasiness",
     "apprehension", "apprehensiveness", "nervousness", "nerves", "perturbation", "foreboding", "the creeps", "the shivers"]


def countwords(words):
    counter = 0
    for word in words:
        counter+= len(re.findall(word, str(f)))
    return counter

if (sys.argv[1] == "mex"):
    data = {'feliz': countwords(happywords), 'triste': countwords(sadwords), 'disgusto': countwords(disgustwords), 'sorpresa': countwords(surprisewords), 'enojado': countwords(angrywords), 'miedo': countwords(fearwords)}
    print "feliz: " + str(countwords(happywords))
    print "triste: " + str(countwords(sadwords))
    print "disgusto: "+ str(countwords(disgustwords))
    print "sorpresa: "+ str(countwords(surprisewords))
    print "enojado: "+ str(countwords(angrywords))
    print "miedo: "+ str(countwords(fearwords))
else:
    data = {'happy': countwords(happywords), 'sad': countwords(sadwords), 'disgust': countwords(disgustwords), 'surprise': countwords(surprisewords), 'angry': countwords(angrywords), 'scary': countwords(fearwords)}
    print "happy: " + str(countwords(happywords))
    print "sad: " + str(countwords(sadwords))
    print "disgust: "+ str(countwords(disgustwords))
    print "surprise: "+ str(countwords(surprisewords))
    print "angry: "+ str(countwords(angrywords))
    print "fear: "+ str(countwords(fearwords))


filename = sys.argv[1] + '.json'

# fear anger disgust happy surprise sad
with open(filename, 'w') as outfile:
    json.dump(data, outfile)
