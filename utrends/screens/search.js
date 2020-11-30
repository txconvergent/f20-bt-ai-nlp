import React from 'react';
import { StyleSheet, Text, View, SafeAreaView, ScrollView } from 'react-native';
import { CategoryCard } from '../components/category_card.js';

export function SearchScreen() {
    return (
      <SafeAreaView style={styles.container}>
        <ScrollView style={styles.scrollView}>
          <View style={styles.cardRow}>
            <CategoryCard category={'General'}/>
            <CategoryCard category={'News'}/>
          </View>

          <View style={styles.cardRow}>
            <CategoryCard category={'COVID-19'}/>
            <CategoryCard category={'Sports'}/>
          </View>

          <View style={styles.cardRow}>
            <CategoryCard category={'Campus Events'}/>
            <CategoryCard category={'Official UT News'}/>
          </View>

          <View style={styles.cardRow}>
            <CategoryCard category={'Twitter'}/>
            <CategoryCard category={'Austin-Area News'}/>
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