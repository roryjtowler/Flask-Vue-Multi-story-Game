<template>
  <div id = "app">

    <button @click.prevent="getStory('1')">Back To Start</button>
    <button @click.prevent="getStory(info.middle.parentID)">Back</button>
    <button @click.prevent="getStory('0')">newstory</button>

    <div class="grid-container">
        <div class="grid-item"></div>
        <div class="grid-item">
          <div v-if="info.top.sentence == '' && info.middle.sentence != '' ">
            <form>
              <input type="text" ref="top">
              <button @click.prevent="handleSubmit('top')">Submit</button>
            </form>
          </div>
          <div v-else-if = "info.middle.sentence != ''">
            <p1> {{info.top.sentence}} </p1>
            <br><br/>
            <button @click.prevent="getStory(info.top.id)">Select Story</button>
          </div>
        </div>

        <div class="grid-item"></div>

        <div class="grid-item">
          <div v-if="info.left.sentence == '' && info.middle.sentence != '' ">
            <form>
              <input type="text" ref="left">
              <button @click.prevent="handleSubmit('left')">Submit</button>
            </form>
          </div>
          <div v-else-if="info.middle.sentence != ''">
            <p1> {{info.left.sentence}} </p1>
            <br><br/>
            <button @click.prevent="getStory(info.left.id)">Select Story</button>
          </div>
        </div>

        <div class="grid-item">
          <div v-if="info.middle.sentence == '' ">
            <form>
              <input type="text" ref="middle">
              <button @click.prevent="handleSubmit('middle')">Submit</button>
            </form>
          </div>
          <div v-else>
            <p1> {{info.middle.sentence}} </p1>
          </div>
        </div>

        <div class="grid-item">
          <div v-if="info.right.sentence == '' && info.middle.sentence != '' ">
            <form>
              <input type="text" ref="right">
              <button @click.prevent="handleSubmit('right')">Submit</button>
            </form>
          </div>
          <div v-else-if="info.middle.sentence != ''">
            <p1> {{info.right.sentence}} </p1>
            <br><br/>
            <button @click.prevent="getStory(info.right.id)">Select Story</button>
          </div>
        </div>

        <div class="grid-item"></div>

        <div class="grid-item">
          <div v-if="info.bottom.sentence == '' && info.middle.sentence != '' ">
            <form>
              <input type="text" ref="bottom">
              <button @click.prevent="handleSubmit('bottom')">Submit</button>
            </form>
          </div>
          <div v-else-if="info.middle.sentence != ''">
            <p1> {{info.bottom.sentence}} </p1>
            <br><br/>
            <button @click.prevent="getStory(info.bottom.id)">Select Story</button>
          </div>
        </div>
        <div class="grid-item"></div>
      </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      info: {
        middle: {
          sentence: '',
          currentID: '1',
          parentID: '',
        },

        top: {
          id: '',
          sentence: '',
        },

        left: {
          id: '',
          sentence: '',
        },

        right: {
          id: '',
          sentence: '',
        },

        bottom: {
          id: '',
          sentence: '',
        },
      },
    };
  },

  methods: {
    sendForm(payload) {
      const path = 'http://localhost:5000/createStory';
      axios.post(path, payload).then((res) => {
        const data = res.data;
        const id = data.id;
        const pos = data.pos;

        this.info[pos].id = id;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },

    handleSubmit(pos) {
      this.info[pos].sentence = this.$refs[pos].value;
      const payload = {
        sentence: this.info[pos].sentence,
        positon: pos,
        currentID: this.info.middle.currentID,
      };
      this.sendForm(payload);
    },

    getStory(ident) {
      const path = 'http://localhost:5000/getStory';
      const payload = {
        id: ident,
      };
      axios.post(path, payload).then((res) => {
        const data = res.data;
        this.info.middle.parentID = data.parentID;
        this.info.middle.sentence = data.middle;
        this.info.middle.currentID = data.currentID;
        this.info.top.sentence = data.top;
        this.info.top.id = data.topID;
        this.info.left.sentence = data.left;
        this.info.left.id = data.leftID;
        this.info.right.sentence = data.right;
        this.info.right.id = data.rightID;
        this.info.bottom.sentence = data.bottom;
        this.info.bottom.id = data.bottomID;
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
      });
    },
  },
};
</script>
