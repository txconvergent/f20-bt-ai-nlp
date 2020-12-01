import React from 'react';
import { StyleSheet, Text, View, SafeAreaView, ScrollView } from 'react-native';

import { SavedEntry } from '../components/saved_entry.js';

export function SavedScreen() {
    return (
      <SafeAreaView style={styles.container}>
        <ScrollView style={styles.scrollView}>
          <SavedEntry text={'Sample body text'} source={'Sample source'}/>
          <SavedEntry text={'Sample body text 2'} source={'Sample source 2'}/>
          <SavedEntry text={'Sample body text'} source={'Sample source'}/>
          <SavedEntry text={'Sample body text 2'} source={'Sample source 2'}/>
          <SavedEntry text={'Sample body text'} source={'Sample source'}/>
          <SavedEntry text={'Sample body text 2'} source={'Sample source 2'}/>
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
    marginTop: 10,
    paddingHorizontal: 10,
  }
});
