import React from 'react';
import { StyleSheet, Text, View, SafeAreaView, ScrollView, TouchableOpacity } from 'react-native';
import { CategoryCard } from '../components/category_card.js';
import { createStackNavigator } from '@react-navigation/stack';
import { NavigationContainer } from '@react-navigation/native';

import { SwipeScreen } from './home.js';
import { SettingsPage } from './settings.js';

import * as RootNavigation from '../RootNavigation.js';

const Stack = createStackNavigator();

export function SearchScreen() {
  return (
    <Stack.Navigator headerMode={"none"}>
      <Stack.Screen name="Home" component={SearchHomeScreen}/>
      <Stack.Screen name="Swipe" component={SwipeScreen}/>
    </Stack.Navigator>
  )
}

export function SearchHomeScreen({navigation}) {
    return (
      <SafeAreaView style={styles.container}>
        <ScrollView style={styles.scrollView}>
          <View style={styles.cardRow}>
            <TouchableOpacity style={styles.cardContainer} activeOpacity={0.7} onPress={() => navigation.navigate("Swipe", {category: 'General'})}>
              <CategoryCard category={'General'}/>
            </TouchableOpacity>
            <TouchableOpacity style={styles.cardContainer} activeOpacity={0.7} onPress={() => navigation.navigate("Swipe", {category: 'News'})}>
              <CategoryCard category={'News'}/>
            </TouchableOpacity>
          </View>

          <View style={styles.cardRow}>
          <TouchableOpacity style={styles.cardContainer} activeOpacity={0.7} onPress={() => navigation.navigate("Swipe", {category: 'COVID-19'})}>
              <CategoryCard category={'COVID-19'}/>
            </TouchableOpacity>
            <TouchableOpacity style={styles.cardContainer} activeOpacity={0.7} onPress={() => navigation.navigate("Swipe", {category: 'Sports'})}>
              <CategoryCard category={'Sports'}/>
            </TouchableOpacity>
          </View>

          <View style={styles.cardRow}>
          <TouchableOpacity style={styles.cardContainer} activeOpacity={0.7} onPress={() => navigation.navigate("Swipe", {category: 'Campus Events'})}>
              <CategoryCard category={'Campus Events'}/>
            </TouchableOpacity>
            <TouchableOpacity style={styles.cardContainer} activeOpacity={0.7} onPress={() => navigation.navigate("Swipe", {category: 'Official UT News'})}>
              <CategoryCard category={'Official UT News'}/>
            </TouchableOpacity>
          </View>

          <View style={styles.cardRow}>
          <TouchableOpacity style={styles.cardContainer} activeOpacity={0.7} onPress={() => navigation.navigate("Swipe", {category: 'Twitter'})}>
              <CategoryCard category={'Twitter'}/>
            </TouchableOpacity>
            <TouchableOpacity style={styles.cardContainer} activeOpacity={0.7} onPress={() => navigation.navigate("Swipe", {category: 'Austin Area News'})}>
              <CategoryCard category={'Austin Area News'}/>
            </TouchableOpacity>
          </View>

        </ScrollView>
      </SafeAreaView>
    );
  }

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'white',
  },

  cardContainer: {
    width: '50%',
    height: '100%',
  },

  scrollView: {
    backgroundColor: 'white',
    marginTop: 30,
  },

  cardRow: {
    backgroundColor: 'white',
    flexDirection: 'row',
    width: '100%',
  }
});